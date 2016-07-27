# Scaffold

Scaffold is a tool for you to setup your project layout. It is based upon a minimal implementation of Django's default template engine.

Scaffold setups up the project according to given templates.

## Why scaffold
Scaffold is highly customizable.  It uses {{ variable }} tag to provide customizable templates, same as Django's template system.

**Note:** variables can be used in **files**, **file names** and even **directories**.

## How to install
You have two options to install it:
### Install from source
1. git clone this repo
2. `cd scafold` directory
3. `tar -zcvf templates.tar.gz templates` to create a `.tar.gz` file
4. Now, you are ready to install it. **Due to some permission issue**, installing scaffold globally is not recommended.
   If you are using virtualenv,  you can run:  
    
   ``python setup.py install``

   Otherwise, you should use:

   ``python setup install --user``

### Install using pip
Similar as above,  if you're using virtualenv, use

``pip install scaffolding`` 

Otherwise use 

``pip install scaffolding --user``

## Usage
* `scaffold list`

scaffold provides some default layout, use this command to list them

* `scaffold show <name>`
	
Given a name listed by `list` command, output it's layout. For example:
```
|-- utils
|    -- __init__.py
|-- README.md
|-- main.py
|-- context
|-- .gitignore
```

* `scaffold show --template=<path>`
	
Similar to above, but not supported yet.

* `scaffold create <name>`
	
Create the project layout based on given template.

* `scaffold create --template=<path>`
	
Similar to above, but not supported yet

* `scaffold locate`
	
Locate scaffold's template directory. You can add you personal tempaltes here.

* `scaffold remove <name>`
	
Remove a template if you don't want it.

**Note:**For a full list of documentation, use ``scaffold -h``

## Create your own templates
You can create your own templates easily. Here is how to do it:

1. use `scaffold locate` to locate the template directory. You should have some default templates in the directory. Here, a template should be a directory in the 'template' directory
2. In each template, there should be a 'context' file, it defines all your variables. Variables can have default values. For example, I will define 2 variables, `app_name` has no default value while `author` has:
```
app_name
author: ME
```

**Note:** `{{ variable }}` tag can be used in files, file names and directories. Check out the default templates for examples.
