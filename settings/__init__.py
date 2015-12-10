from settings.base import *

if 'DOCKER_RUN' in os.environ:
    from settings.docker import *

if 'OPENSHIFT_REPO_DIR' in os.environ:
    from settings.openshift import *
