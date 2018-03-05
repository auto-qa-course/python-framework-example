# Automation framework creation checklist

1. Create git repo
2. Create README.md file. Start creating documentation in parallel with framework creation. It could contain information about:
    * list of tools\libraries used, possibly with installation instructions
    * test configuration instructions
    * test execution commands and options
3. Create .gitignore file
4. Define packages and folders structure
    * configurations (parameterized run, env variables, configuration files)
    * tests (specs, features, etc)
        * Here also need to be defined some structure. For example one can use feature -> story -> test case structure
    * app specific classes and methods 
        * api (can also split api and services operations)
        * page objects (can also split page elements locators and operations of page)
    * helper classes and methods (BP: wrapp related methods into one class\module\package)
        * constants
        * logger
        * config reader
        * time, file manipulations helpers
        * data generation helpers
5. Сhoose reporting tool if needed, setup and integrate 
6. Do not commit: 
    * compiled class files
    * reports folder
    * .idea folder ( should be in .gitignore )
    * .git folder  ( should be in .gitignore )
