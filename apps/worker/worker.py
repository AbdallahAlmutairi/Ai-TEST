"""Entry point for executing worker tasks."""

from tasks import backtest_job, fetch_data, train


def main() -> None:
    """Run a few sample tasks."""
    print(fetch_data.fetch("AAPL"))
    print(train.train())
    print(backtest_job.backtest())


if __name__ == "__main__":
    main()
