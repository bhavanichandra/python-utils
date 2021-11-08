OS = mac
VENV=.venv
COMMIT_MESSAGE=
BRANCH=main
APP_NAME=

ifeq ($(OS), mac)
	PYTHON = $(VENV)/bin/python
	PIP = $(VENV)/bin/pip
else
	PYTHON = $(VENV)/Scripts/python
	PIP = $(VENV)/Scripts/pip
endif

init: 
	touch requirements.txt
	echo 'Add .gitignore'

run: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

djangoinit: 
	django-admin startproject $(APP_NAME) .

update-requirements: 
	rm requirements.txt
	$(PIP) freeze > requirements.txt

commit-push: update-requirements
	git add --all
	git commit -m "$(COMMIT_MESSAGE)"
	git push pi $(BRANCH)

clean:
	find . -type d -name __pycache__ -prune -exec rm -r {} +
	
