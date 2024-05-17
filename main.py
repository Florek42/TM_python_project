import os

def create_project_structure(project_name):
  """
  Utwórz strukturę katalogów dla gry 3D.

  Args:
    project_name: Nazwa projektu gry.
  """

  # Utwórz główny katalog projektu.
  project_dir = os.path.join(os.getcwd(), project_name)
  if not os.path.exists(project_dir):
    os.makedirs(project_dir)

  # Utwórz podkatalogi.
  subdirs = [
      "documentation",
      "sound",
      "graphics",
      "code",
  ]
  for subdir in subdirs:
    os.makedirs(os.path.join(project_dir, subdir))

  # Utwórz podkatalogi w "code".
  code_subdirs = [
      "mechanics",
      "entities",
      "world",
      "ui",
  ]
  for subdir in code_subdirs:
    os.makedirs(os.path.join(project_dir, "code", subdir))

  # Utwórz pliki konfiguracyjne.
  with open(os.path.join(project_dir, "config.py"), "w"):
    pass

  # Utwórz plik uruchamiający.
  with open(os.path.join(project_dir, "run.py"), "w"):
    pass

if __name__ == "__main__":
  project_name = input("Podaj nazwę swojego projektu gry 3D: ")
  create_project_structure(project_name)
  print(f"Struktura katalogów dla gry '{project_name}' została utworzona!")
