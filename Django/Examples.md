# Django Examples
###  Getting telemetry data to show in your console
For telemetry to show in your terminal, your `manage.py` file should look like this:

```python
import os
import sys
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk import resources

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todolist_project.settings")

    resource = resources.Resource(attributes={
        resources.SERVICE_NAME: "your-service-name",
        resources.SERVICE_VERSION: "1.0.0"
    })

    trace_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(trace_provider)

    console_exporter = ConsoleSpanExporter()

    span_processor = BatchSpanProcessor(console_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
```

### Example applications
This repository contains two example applications, one showing [automatic instrumentation](https://github.com/JessicaGarson/Introduction-to-OpenTelemetry-with-Django/tree/main/automatic-instrumentation/todolist_project) and the other [manual instrumentation](https://github.com/JessicaGarson/Introduction-to-OpenTelemetry-with-Django/tree/main/manual-instrumentation/todolist_project) using OpenTelemetry, sending the results into Elastic. Both applications are simple to-do list applications made with Django.

#### Getting started
Before you can use either, you will need to do the following:

- Create a virtual environment.

  Mac:
  
  ```
  python -m venv venv
  source venv/bin/activate
  ```

  Windows:

  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```

- Install the required packages:

  ``` 
  pip install -r requirements.txt
  ```

- Move the `env.example` into the root of whichever example you want to run. Be sure to update it with your own credentials and save it as `.env`. 

#### Running the example applications

You can use the following command to run each example application:

```
python manage.py runserver
```

#### Viewing the results in Elastic
If everything is working as intended, you should be able to see observablity data in the Services section in Elastic APM.
