# eslint-onboarder
### A little script that helps your team deal with onboarding an existing project to strict ESLint rules.
It prepends a directive to disable ESLint and a TODO to re-enable it in the project's JavaScript files. False positives and false negatives abound, but it's been working alright overall.

### USAGE
```
cd project-root
python eslint_disable_with_warning.py --verbose
```
