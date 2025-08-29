if __name__ == "__main__":  # pragma: no cover
    import importlib.util
    import pkgutil
    from inspect import getmembers, isclass
    from ingest_classes.base_class import BaseClass

    class_dict = {}

    parent_package = __name__

    for module_finder, module_name, is_pkg in pkgutil.walk_packages(__path__):
        if module_name == "base_class":
            continue

        full_module_name = f"{parent_package}.{module_name}"

        spec = importlib.util.find_spec(full_module_name)
        if spec is not None and spec.loader is not None:
            _module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(_module)

            for _cname, _cls in getmembers(_module, isclass):
                if issubclass(_cls, BaseClass) and _cls is not BaseClass:
                    class_dict[_cname] = _cls
