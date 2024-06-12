import pkg_resources

def create_requirements_file(filename='requirements.txt'):
    installed_packages = pkg_resources.working_set
    with open(filename, 'w') as f:
        for package in installed_packages:
            f.write(f"{package.key}=={package.version}\n")
    print(f"{filename} has been created successfully.")

if __name__ == '__main__':
    create_requirements_file()