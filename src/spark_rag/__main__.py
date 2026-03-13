import argparse

from spark_rag.ingest import ingest_file

def main():
    parser=argparse.ArgumentParser(prog="spark_rag")
    sub = parser.add_subparsers(dest="command")

    ingest = sub.add_parser("ingest", help="Ingest a document (placeholder)")
    ingest.add_argument("path")

    args = parser.parse_args()

    if args.command == "ingest":
        print(ingest_file(path=args.path))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
