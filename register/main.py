import json
from typing import Any, Callable
from register import get_registry, _register

import typer    
import pkgutil
import importlib
app = typer.Typer()

type Data = dict[str, Any]
type ExportFn = Callable[[Data], None]

def load_text_commands() -> None:
    import commands.text
    for _, module_name, _ in pkgutil.iter_modules(commands.text.__path__):
        importlib.import_module(f'commands.text.{module_name}')

def load_plugins() -> None:
    import plugins
    for _, module_name, _ in pkgutil.iter_modules(plugins.__path__):
        importlib.import_module(f"plugins.{module_name}")


# def register_with_typer() -> None:
#     group_apps: dict[str, typer.Typer] = {}

#     for group, name, func in get_registry():
#         if group not in group_apps:
#             group_apps[group] = typer.Typer()
#             app.add_typer(group_apps[group], name = group)
#         group_apps[group].command(name)(func)


def register_with_typer() -> None:
    group_apps: dict[str, typer.Typer] = {}
    # print("开始绑定命令到 Typer...")
    for group, name, func in get_registry():
        # print(f"处理命令：group={group}, name={name}, 函数名={func.__name__}")
        if group not in group_apps:
            group_apps[group] = typer.Typer()
            app.add_typer(group_apps[group], name=group)
            # print(f"已创建并添加分组：{group}")
        # 绑定命令
        group_apps[group].command(name)(func)
        # print(f"已绑定命令：{group}.{name}")
    # print("命令绑定完成")
# exporters: dict[str, ExportFn] = {
# }



# def register_exporter(format: str) -> Callable[[ExportFn], ExportFn]:
#     def decorator(fn: ExportFn) -> ExportFn:
#         @wraps(fn)
#         def wrapper(*args:Any, **kwargs: Any) -> Any:
#             print(f'i have been registered')
#             return fn(*args, **kwargs)
        
#         exporters[format] = wrapper
#         print(f"已注册格式: {format}，当前 exporters: {list(exporters.keys())}")
#         return wrapper
#     return decorator




# @register_exporter('pdf')
# def export_pdf(data: Data) ->None:
#     print(f"Exporting data to PDF: {data}")

# @register_exporter('csv')
# def export_csv(data: Data) ->None:
#     print(f"Exporting data to CSV: {data}")

# @register_exporter('json')
# def export_json(data: Data) ->None:
#     print(f"Exporting data to json: {data}")
#     print(json.dumps(data, indent=2 ))


# def export_data(data: Data, format: str) -> None:
#     exporter = exporters.get(format)
#     if exporter is None:
#         raise ValueError(f"❌No exporter found for format:{format}")
#     exporter(data)


def main() -> None:
    # sample_data: Data = {"name":"Alice", "age": 30}
    # export_data(sample_data, 'pdf')
    # export_data(sample_data, 'csv')
    # export_data(sample_data, 'json')
    try:
        load_text_commands()
        load_plugins()
        register_with_typer()
        app()
    except Exception as e:
        print(e)

if __name__ == "__main__":

    main()


