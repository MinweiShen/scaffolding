# Scaffold

Scaffold is a tool for you to setup your project layout. It is based upon a minimal implementation of Django's default template engine.

Scaffold setups up the project based on given templates.

## Why scaffold
Scaffold is highly customizable.  It uses {{ variable }} tag to provide customizable templates, same as Django's template system.

**Note:** variables can be used in **files**, **file names** and even **directories**.

## How to install
You have two options to install it:
1.  Install from source:
	1.  git clone this repo
	2.  `cd scafold` directory
	3.  `tar -zcvf templates.tar.gz templates` to create a `.tar.gz` file
	4.  Now, you are ready to install it. **Due to some permission issue**, installing scaffold globally is not recommended. 
	If you are using virtualenv,  you can run:  
	``python setup.py install``.
	Otherwise, you should use 
	``python setup install --user``

2. Install using pip
	1. Similar as above,  if you're using virtualenv, use
	``pip install scaffolding`` 
	Otherwise use 
	``pip install scaffolding --user``

## Usage
1. `scaffold list`
	scaffold provides some default layout, use this command to list them
2. `scaffold show <name>`
	Given a name listed by `list` command, output it's layout. For example:
	```
		|-- utils
		|    -- __init__.py
		|-- README.md
		|-- main.py
		|-- context
		|-- .gitignore

	```
3. `  scaffold show --template=<path>`
	Similar to above, not supported yet.
4. `  scaffold create <name>`
	Create the project layout based on given template.
5.   `scaffold create --template=<path>`
	Similar to above, not supported yet
6. `scaffold locate`
	Output scaffold's template directory. You can add you personal tempaltes here.
7. `  scaffold remove <name>`
	Remove a template if you don't want it.

For a full list of documentation, use ``scaffold -h``

## Create your own templates
You can create your own templates easily. Here is how to do it:
1. use `scaffold locate` to locate the template directory. You should have some default templates in the directory. Here, a template should be a directory in the 'template' directory
2. In each template, there should be a 'context' file, it defines all your variables. Variables can have default values. For example, I will define 2 variables, `app_name` has no default value while `author` has.
```
app_name
author: Me
```
3. You can use your variables using `{{ variable }}` tag. It can be used in files, file names and directories.


**Note:** Check out the default templates for examples.