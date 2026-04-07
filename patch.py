import sys

with open('submit_acmoj/acmoj_client.py', 'r') as f:
    content = f.read()

content = content.replace('''    submit_parser.add_argument("--code-file", type=str, required=True,
                               help="Path to the source code file")''', '''    submit_parser.add_argument("--git-url", type=str, required=True,
                               help="Git repository URL")''')

content = content.replace('''        try:
            with open(args.code_file, 'r', encoding='utf-8') as f:
                code_text = f.read()
        except FileNotFoundError:
            print(f"Error: Code file not found at {args.code_file}")
            exit(1)
        except Exception as e:
            print(f"Error: Failed to read code file: {e}")
            exit(1)

        result = client.submit_git(args.problem_id, args.code_file)''', '''        result = client.submit_git(args.problem_id, args.git_url)''')

with open('submit_acmoj/acmoj_client.py', 'w') as f:
    f.write(content)
