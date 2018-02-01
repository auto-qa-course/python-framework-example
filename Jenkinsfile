currentBuild.displayName = "${currentBuild.displayName}: ${pipeline_image}"
currentBuild.description = "${pipeline_image}"

pipeline {
    parameters {
        string(name: 'TEST_REPO_URL', defaultValue: 'https://github.com/auto-qa-course/python-framework-example.git')
        string(name: 'TEST_BRANCH', defaultValue: 'lesson3')
    }

    options {
        timestamps()
    }

    environment {
        QA_ENV='QA'
        STAGE_ENV='Stage'
    }

    stages {

        stage(''Build & Unit tests'') {
            //
        }

        stage('SonarQube Scan') {
            //
        }

        stage('Publish') {
             //
        }

        stage('Deploy to QA env') {
             //
        }

        stage("Integration testing") {
            steps {
                git url: '$TEST_REPO_URL', branch: '${TEST_BRANCH}'

                sh('''
                    rm out_docker_results/**/*.json || echo 'no json files'

                    docker build -t automation_demo .

                    mkdir out_docker_results || echo 'out_docker_results dir exists'

                    docker run -v $(pwd)/out_docker_results:/out:rw -e "ENVIRONMENT=$QA_ENV" -e "TEST_TYPE=api" -e "RESULTS_FOLDER=outputs" -i automation_demo /bin/bash -c "pytest test/api --alluredir /out"
                ''')

                allure includeProperties: false, jdk: '', results: [[path: 'out_docker_results']]
            }
        }

        stage('Request approval for deploy to Stage') {
            steps {
                script {
                    timeout(time:10, unit:'MINUTES') {
                        while (true) {
                            userPasswordInput = input(id: 'userPasswordInput',
                                message: 'Please approve deploy to Stage. Enter password to proceed.',
                                parameters: [[$class: 'StringParameterDefinition', defaultValue: '',  name: 'Password']])
                            if (userPasswordInput=='Yes') { break }
                        }
                    }
                }
            }
        }

        stage('Deploy to Stage env') {
             //
        }
    }

    post {
        failure {
            allure includeProperties: false, jdk: '', results: [[path: 'out_docker_results']]
        }
    }
}