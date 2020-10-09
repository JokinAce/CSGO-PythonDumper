import os
from datetime import date
from github import Github

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

# Push the files to Github
def SendFiles(datum):
    g = Github("API Key (Personal Access Tokens)")
    repo = g.get_repo("YourName/Repositoryname")
    files_list = ["csgo.cs","csgo.hpp","csgo.json","csgo.min.json","csgo.toml","csgo.vb","csgo.yaml"]
    for x in files_list:
        print("Updating " + x)
        contents = repo.get_contents(x, ref="master")
        repo.update_file(contents.path, "✨ CS:GO Offsets Update " + datum, file_get_contents(x), contents.sha, branch="master")

if __name__ == "__main__":
	print("Opening HazeDumper")
	os.system("hazedumper-v2.4.1.exe")

	print("Uploading to Github")
	SendFiles(str(date.today()))
