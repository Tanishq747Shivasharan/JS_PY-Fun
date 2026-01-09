# NPM Understanding.
<h4>npm is the package manager for Node.js that lets me install, update, and manage libraries (packages) your project needs.
It also helps you run project scripts and keep dependencies organized using package.json.<h4>

## Installing and uninstalling anything basics & advanced.

### installation
```md
npm i <package_name> (OR npm install <package_name>)
```
### uninstallation 
```md
npm uninstall <package_name>
```
### Specific version
```md
npm i <package_name>@<version>
```
### Global installation
```md
npm i -g <package_name>
```
### Updating packages
```md
npm update <package_name>
```
### Updating all packages
```md
npm update
```
### Updating to the latest version
```md
npm update <package_name> --latest
```
### Updating to the latest version of all packages
```md
npm update --latest
```
### Updating to the latest version of all packages globally
```md
npm update -g
```
### Updating to the latest version of all packages globally
```md
npm update -g --latest
```

## Understanding node_modules
The node_modules folder stores all the libraries and code that npm installs for my projects.
My app uses this folder to import and run those dependencies, so I usually don’t edit it manually.

**dependencies** are packages your app needs to run in production (users need them).<br>
**devDependencies** are only needed during development, like testing, building, or formatting tools.(The thing that is not needed when the project is uploaded or deployed. )

## Scripts in package.json
Scripts in package.json are shortcuts for commands you run with 
```md
npm run <name>
```
Built-in ones like **start** and **test** are standard, while custom scripts automate your own tasks **(build, dev, lint)**.

## Work in Progress

JS_PYFun is an evolving repository.
New projects, refinements, and improvements are added regularly as learning continues.

---

## Contributions

This repository is primarily for personal learning and experimentation.
Suggestions and constructive feedback are always welcome.

---

## If You Find This Useful

Consider starring ⭐ the repository to track progress and support the work.

---

**Happy Coding**
*Build. Break. Learn. Repeat.*
