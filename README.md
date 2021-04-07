# zap-runner
Runner for OSWAP ZAP scan.

# Usage in a Rancher pipeline
```
- name: "ZAP test"
  steps:
  - applyAppConfig:
      catalogTemplate: "cattle-global-data:iii-dev-charts3-test-zap"
      version: "0.1.0"
      name: "${CICD_GIT_REPO_NAME}-${CICD_GIT_BRANCH}-zap"
      targetNamespace: "${CICD_GIT_REPO_NAME}"
      answers:
        git.branch: "${CICD_GIT_BRANCH}"
        git.commitID: "${CICD_GIT_COMMIT}"
        git.repoName: "${CICD_GIT_REPO_NAME}"
        git.url: "${CICD_GIT_URL}"
        pipeline.sequence: "${CICD_EXECUTION_SEQUENCE}"
        web.deployName: "${CICD_GIT_REPO_NAME}-${CICD_GIT_BRANCH}-web"
        web.port: 8080
```
