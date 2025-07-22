# Django Examples

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

  ```
  OTEL_EXPORTER_OTLP_HEADERS="Authorization=ApiKey%20yourapikey"
  OTEL_EXPORTER_OTLP_ENDPOINT="https://your/host/endpoint"
  ```

#### Running the example applications

You can use the following command to run each example application:

```
python manage.py runserver
```

#### Viewing the results in Elastic
If everything is working as intended, you should be able to see observablity data in the Services section in Elastic APM.
