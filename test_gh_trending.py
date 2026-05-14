#!/usr/bin/env python3
"""
gh-trending-all 测试文件
"""

import pytest
from gh_trending_all import (
    GitHubRepo,
    format_number,
    get_date_range,
)


class TestFormatNumber:
    """测试数字格式化"""

    def test_small_number(self):
        assert format_number(100) == "100"

    def test_thousand_with_decimal(self):
        assert format_number(1500) == "1.5k"

    def test_thousand_rounding(self):
        assert format_number(1523) == "1.5k"

    def test_large_number(self):
        assert format_number(102000) == "102.0k"


class TestGetDateRange:
    """测试日期范围获取"""

    def test_daily(self):
        assert get_date_range("daily") == "today"

    def test_weekly(self):
        assert get_date_range("weekly") == "7 days ago"

    def test_monthly(self):
        assert get_date_range("monthly") == "30 days ago"

    def test_default(self):
        assert get_date_range("unknown") == "today"


class TestGitHubRepo:
    """测试 GitHub 仓库数据类"""

    def test_repo_creation(self):
        repo = GitHubRepo(
            name="test/repo",
            description="Test description",
            language="Python",
            stars=100,
            forks=10,
            author="test",
            url="https://github.com/test/repo"
        )
        assert repo.name == "test/repo"
        assert repo.description == "Test description"
        assert repo.language == "Python"
        assert repo.stars == 100
        assert repo.forks == 10

    def test_repo_empty_description(self):
        repo = GitHubRepo(
            name="test/repo",
            description="",
            language="Python",
            stars=100,
            forks=10,
            author="test",
            url="https://github.com/test/repo"
        )
        assert repo.description == ""


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
