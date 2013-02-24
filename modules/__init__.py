import modules
import module
import importlib
import glob
import os


def all_modules():
    '''Return a list of all feature modules for use in godfrey.'''
    print "__file__:", os.path.dirname(__file__)
    pyfiles = glob.glob(os.path.dirname(__file__) + "/*.py")
    pyfiles = [pyfile.replace(os.path.dirname(__file__) + "/", "") for pyfile in pyfiles]
    pyfiles = [pyfile.replace(".py", "") for pyfile in pyfiles]
    pyfiles = [pyfile for pyfile in pyfiles if not pyfile.startswith("__")]
    print "pyfiles:", pyfiles
    feature_modules = [importlib.import_module("modules." + pyfile) for pyfile in pyfiles]
    feature_classes = []
    for m in feature_modules:
        feature_classes.extend([getattr(m, x) for x in dir(m) if not x.startswith("__") and not x == "module"])
    feature_classes = [x() for x in feature_classes if issubclass(x, module.Module)]

    return feature_classes
