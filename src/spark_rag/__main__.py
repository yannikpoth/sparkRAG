import argparse

def main():
    parser=argparse.ArgumentParser(prog="spark_rag")
    sub = parser.add_subparsers(dest="command")

    ingest = sub.add_parser("ingest", help="Ingest a document (placeholder)")
    ingest.add_argument("path")

    args = parser.parse_args()

    if args.command == "ingest":
        print(f"[ingest] path={args.path}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
