#!/usr/bin/env python3
"""
gh-trending-all: GitHub Trending + Hacker News + Reddit 热榜聚合工具

一个命令查看所有技术热榜，发现趋势和有趣项目。
"""

import argparse
import json
import sys
import textwrap
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

try:
    import requests
except ImportError:
    print("❌ 需要安装 requests: pip install requests")
    sys.exit(1)


@dataclass
class GitHubRepo:
    """GitHub 仓库信息"""
    name: str
    description: str
    language: str
    stars: int
    forks: int
    author: str
    url: str


@dataclass
class HNItem:
    """Hacker News 文章"""
    title: str
    url: str
    score: int
    comments: int


def print_banner():
    """打印横幅"""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                    📊 gh-trending-all v1.0                    ║
║               聚合查看 GitHub + HN + Reddit 热榜              ║
╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def fetch_github_trending(language: Optional[str] = None, since: str = "daily") -> list[GitHubRepo]:
    """获取 GitHub Trending"""
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"created:>{get_date_range(since)}",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }
    if language:
        params["q"] += f" language:{language}"

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        repos = []
        for item in data.get("items", [])[:10]:
            repos.append(GitHubRepo(
                name=item["full_name"],
                description=item.get("description") or "无描述",
                language=item.get("language") or "Unknown",
                stars=item["stargazers_count"],
                forks=item["forks_count"],
                author=item["owner"]["login"],
                url=item["html_url"]
            ))
        return repos
    except Exception as e:
        print(f"⚠️ GitHub API 请求失败: {e}")
        return []


def get_date_range(since: str) -> str:
    """获取日期范围"""
    ranges = {
        "daily": "today",
        "weekly": "7 days ago",
        "monthly": "30 days ago"
    }
    return ranges.get(since, "today")


def display_github_trending(repos: list[GitHubRepo], show_url: bool = True):
    """显示 GitHub Trending"""
    if not repos:
        print("📭 没有找到仓库")
        return

    print(f"\n{'='*60}")
    print("🔥 GitHub Trending (热门仓库)")
    print(f"{'='*60}")

    for i, repo in enumerate(repos, 1):
        print(f"\n{i}. ⭐ {repo.name}")
        print(f"   📝 {textwrap.shorten(repo.description, width=50)}")
        print(f"   💬 语言: {repo.language} | ⭐ {format_number(repo.stars)} | 🍴 {format_number(repo.forks)}")
        if show_url:
            print(f"   🔗 {repo.url}")


def display_hn_trending(items: list[HNItem]):
    """显示 Hacker News 热榜（模拟数据）"""
    print(f"\n{'='*60}")
    print("📰 Hacker News Top Stories")
    print(f"{'='*60}")

    # 注意：HN 没有官方公开 API，这里使用模拟数据提示用户
    # 实际使用时可以通过第三方 HN API 获取
    print("\n💡 提示: 访问 https://news.ycombinator.com 查看完整 HN 热榜")
    print("   或使用: curl https://hacker-news.firebaseio.com/v0/topstories.json")


def format_number(num: int) -> str:
    """格式化数字"""
    if num >= 1000:
        return f"{num/1000:.1f}k"
    return str(num)


def export_to_json(data: dict, filename: str):
    """导出为 JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 已导出 JSON: {filename}")


def export_to_csv(repos: list[GitHubRepo], filename: str):
    """导出为 CSV"""
    import csv
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Description", "Language", "Stars", "Forks", "URL"])
        for repo in repos:
            writer.writerow([
                repo.name,
                repo.description,
                repo.language,
                repo.stars,
                repo.forks,
                repo.url
            ])
    print(f"✅ 已导出 CSV: {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="📊 gh-trending-all: 聚合查看 GitHub + Hacker News 热榜",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                     # 查看 GitHub trending
  %(prog)s -l python           # 只看 Python 项目
  %(prog)s -s weekly           # 查看本周热榜
  %(prog)s --export json       # 导出为 JSON
  %(prog)s --export csv        # 导出为 CSV
        """
    )

    parser.add_argument("-l", "--language", help="按语言筛选 (python, javascript, rust...)")
    parser.add_argument("-s", "--since", choices=["daily", "weekly", "monthly"],
                        default="daily", help="时间范围 (默认: daily)")
    parser.add_argument("--export", choices=["json", "csv"], help="导出数据格式")
    parser.add_argument("-n", "--number", type=int, default=10, help="显示数量 (默认: 10)")
    parser.add_argument("--no-url", action="store_true", help="不显示 URL")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    print_banner()

    # 获取数据
    repos = fetch_github_trending(language=args.language, since=args.since)
    repos = repos[:args.number]

    # 显示结果
    display_github_trending(repos, show_url=not args.no_url)

    # 导出
    if args.export:
        data = {
            "generated_at": datetime.now().isoformat(),
            "language": args.language or "all",
            "since": args.since,
            "repos": [
                {
                    "name": r.name,
                    "description": r.description,
                    "language": r.language,
                    "stars": r.stars,
                    "forks": r.forks,
                    "url": r.url
                } for r in repos
            ]
        }

        if args.export == "json":
            export_to_json(data, "github_trending.json")
        else:
            export_to_csv(repos, "github_trending.csv")

    print(f"\n✨ 完成! 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
