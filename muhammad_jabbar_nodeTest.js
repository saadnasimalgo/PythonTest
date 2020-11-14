module.exports = {
    "sparkCommand": "spark-submit",
    "spark": {
        "deployMode": "client",
        "packages": "packages1,packages2",
        "jars": "jar1",
        "pyFiles": "python_file1.py,python_file2.py"
    },
    "spark_application": {
        "app": "spark_file.py",
        "appName": "Name of spark job",
        "options": {
            "executor-memory": "4g",
            "total-executor-cores": "2"
        },
        "args": {
            "arg1": "value1",
            "arg2": "value2"
        }
    },
    "current" : {
        "batchId": "b0543ed0-025c-11eb-90bf-6194a2a2d5ea",
        "fileName": "any_file_name.csv",
        "s3" : {
            "bucket" : "main_storage",
            "key": "b0543ed0-025c-11eb-90bf-6194a2a2d5ea/raw/any_file_name.csv"
        },
        "fileExtension" : 'csv',
    }
}
