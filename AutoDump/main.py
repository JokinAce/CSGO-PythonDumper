import os, requests, json
from datetime import date
from github import Github

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

# Push the files to Github
def SendFiles(datum):
    g = Github("a5d9e169ddfdf16b242d5fc620dd5798233c4b27")
    repo = g.get_repo("JokinAce/CSGO-Offsets")
    files_list = ["csgo.cs","csgo.hpp","csgo.json","csgo.min.json","csgo.toml","csgo.vb","csgo.yaml","csgo.py"]
    for x in files_list:
        print("Updating " + x)
        contents = repo.get_contents(x, ref="master")
        repo.update_file(contents.path, "✨ CS:GO Offsets Update " + datum, file_get_contents(x), contents.sha, branch="master")

if __name__ == "__main__":
    print("Opening HazeDumper")
    os.system("hazedumper-v2.4.1.exe")

    allah = json.loads(open("csgo.json").read())
    with open("csgo.py","w") as f:
        for x in allah["signatures"]:
            f.write(x + " = (" + hex(allah["signatures"][x]) + ")\n")

        for x in allah["netvars"]:
            f.write(x + " = (" + hex(allah["netvars"][x]) + ")\n")
        f.close()

    print("Uploading to Github")
    SendFiles(str(date.today()))
