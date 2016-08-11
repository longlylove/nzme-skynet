#!groovy

node {

    def err = null
    currentBuild.result = "SUCCESS"
    PKG_VERSION = sh (
        script : 'python setup.py --version',
        returnStdout: true
    ).trim()
    PKG_NAME = sh (
        sript = 'python setup.py --fullname',
        returnStdout: true
    ).trim()
    PKG_PATH = "dist/${PKG_NAME}.tar.gz"

    try {

        stage 'Checkout'
            checkout scm

        stage 'Python Requirements'
            sh """
            if [ ! -d "venv" ]
                then
                    virtualenv --no-site-packages venv
                fi
            """
            sh "./venv/bin/pip install -r requirements.txt"

        stage 'Nodejs npm install'
            sh 'node -v'
            sh 'npm prune'
            sh 'npm install'

        stage 'Install phantomJS node module'
            sh 'npm install phantomjs'

        stage 'Test'
            sh """
                . venv/bin/active
                cd test
                py.test
            """

        stage 'Create dist package'
            sh """
                python setup.py sdist
            """

        stage 'Upload artifact to gemfury'
            """
                fury push ${PKG_PATH}
            """

        stage 'Finish'

    }
    catch (caughtError) {

        err = caughtError
        currentBuild.result = "FAILURE"

    }
    finally {

        if (err) {
            throw err
        }
    }
}