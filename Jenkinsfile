#!groovy

node {

    try{
        stage 'Checkout'
            checkout scm
            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            telegramSend "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"
    }
    catch (err) {
        telegramSend "Jenkins generic task error"
        throw err
    }

    try {

        stage 'Test'
            sh 'python3 -m venv env'
            sh '. env/bin/activate'
            sh 'env/bin/pip install -r api/requirements.txt'
            sh 'env/bin/python3 api/src/manage.py test'

        // stage 'Deploy'
        //    sh './deployment/deploy_prod.sh'

        stage 'Publish results'
            telegramSend "Jenkins task completed"
    }

    catch (err) {
        telegramSend "Jenkins django task error"
        throw err
    }

    try {

        stage 'Test'
            sh 'python3 -m venv env'
            sh '. env/bin/activate'
            sh 'env/bin/pip install -r api/requirements.txt'
            sh 'cd api/src; env/bin/python3 manage.py test'

        // stage 'Deploy'
        //    sh './deployment/deploy_prod.sh'

        stage 'Publish results'
            telegramSend "Jenkins task completed"
    }

    catch (err) {
        telegramSend "Jenkins react task error"
        throw err
    }

}