2026-02-24T18:15:49.794408255Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 147, in retry_target
2026-02-24T18:15:49.794410746Z     result = target()
2026-02-24T18:15:49.794413726Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout
2026-02-24T18:15:49.794416296Z     return func(*args, **kwargs)
2026-02-24T18:15:49.794418836Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/grpc_helpers.py", line 77, in error_remapped_callable
2026-02-24T18:15:49.794421366Z     raise exceptions.from_grpc_error(exc) from exc
2026-02-24T18:15:49.794438206Z google.api_core.exceptions.NotFound: 404 models/gemini-pro is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.
2026-02-24T18:15:49.794685971Z Error occurred: 404 models/gemini-pro is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.
2026-02-24T18:15:49.794703301Z INFO:     121.182.26.226:0 - "POST /chat HTTP/1.1" 500 Internal Server Error
2026-02-24T18:16:02.834219883Z INFO:     Shutting down
2026-02-24T18:16:02.934806281Z INFO:     Waiting for application shutdown.
2026-02-24T18:16:02.934946613Z INFO:     Application shutdown complete.
2026-02-24T18:16:02.935040485Z INFO:     Finished server process [56]
2026-02-24T18:17:44.78917266Z ==> Deploying...
2026-02-24T18:17:44.861896738Z ==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance
2026-02-24T18:18:16.659104714Z ==> Running 'uvicorn app:app --host 0.0.0.0 --port $PORT'
2026-02-24T18:18:31.15478937Z /opt/render/project/src/app.py:7: FutureWarning: 
2026-02-24T18:18:31.154809201Z 
2026-02-24T18:18:31.154813622Z All support for the `google.generativeai` package has ended. It will no longer be receiving 
2026-02-24T18:18:31.154817672Z updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
2026-02-24T18:18:31.154821472Z See README for more details:
2026-02-24T18:18:31.154824413Z 
2026-02-24T18:18:31.154827223Z https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md
2026-02-24T18:18:31.154829953Z 
2026-02-24T18:18:31.154833343Z   import google.generativeai as genai
2026-02-24T18:18:31.755959296Z INFO:     Started server process [56]
2026-02-24T18:18:31.755994558Z INFO:     Waiting for application startup.
2026-02-24T18:18:31.756348654Z INFO:     Application startup complete.
2026-02-24T18:18:31.756648235Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2026-02-24T18:18:31.887074461Z --- 사용 가능한 모델 목록 ---
2026-02-24T18:18:31.887100593Z 사용 가능 모델: models/gemini-2.5-flash
2026-02-24T18:18:31.887105493Z 사용 가능 모델: models/gemini-2.5-pro
2026-02-24T18:18:31.887109914Z 사용 가능 모델: models/gemini-2.0-flash
2026-02-24T18:18:31.887113944Z 사용 가능 모델: models/gemini-2.0-flash-001
2026-02-24T18:18:31.887117664Z 사용 가능 모델: models/gemini-2.0-flash-exp-image-generation
2026-02-24T18:18:31.887120485Z 사용 가능 모델: models/gemini-2.0-flash-lite-001
2026-02-24T18:18:31.887123355Z 사용 가능 모델: models/gemini-2.0-flash-lite
2026-02-24T18:18:31.887126095Z 사용 가능 모델: models/gemini-2.5-flash-preview-tts
2026-02-24T18:18:31.887129855Z 사용 가능 모델: models/gemini-2.5-pro-preview-tts
2026-02-24T18:18:31.887134046Z 사용 가능 모델: models/gemma-3-1b-it
2026-02-24T18:18:31.887138106Z 사용 가능 모델: models/gemma-3-4b-it
2026-02-24T18:18:31.887141846Z 사용 가능 모델: models/gemma-3-12b-it
2026-02-24T18:18:31.887145666Z 사용 가능 모델: models/gemma-3-27b-it
2026-02-24T18:18:31.887149347Z 사용 가능 모델: models/gemma-3n-e4b-it
2026-02-24T18:18:31.887153227Z 사용 가능 모델: models/gemma-3n-e2b-it
2026-02-24T18:18:31.887156837Z 사용 가능 모델: models/gemini-flash-latest
2026-02-24T18:18:31.887163628Z 사용 가능 모델: models/gemini-flash-lite-latest
2026-02-24T18:18:31.887168118Z 사용 가능 모델: models/gemini-pro-latest
2026-02-24T18:18:31.887172828Z 사용 가능 모델: models/gemini-2.5-flash-lite
2026-02-24T18:18:31.887176709Z 사용 가능 모델: models/gemini-2.5-flash-image
2026-02-24T18:18:31.887179639Z 사용 가능 모델: models/gemini-2.5-flash-lite-preview-09-2025
2026-02-24T18:18:31.887182429Z 사용 가능 모델: models/gemini-3-pro-preview
2026-02-24T18:18:31.887185219Z 사용 가능 모델: models/gemini-3-flash-preview
2026-02-24T18:18:31.887187979Z 사용 가능 모델: models/gemini-3.1-pro-preview
2026-02-24T18:18:31.88719075Z 사용 가능 모델: models/gemini-3.1-pro-preview-customtools
2026-02-24T18:18:31.88719365Z 사용 가능 모델: models/gemini-3-pro-image-preview
2026-02-24T18:18:31.88719637Z 사용 가능 모델: models/nano-banana-pro-preview
2026-02-24T18:18:31.88719919Z 사용 가능 모델: models/gemini-robotics-er-1.5-preview
2026-02-24T18:18:31.88720198Z 사용 가능 모델: models/gemini-2.5-computer-use-preview-10-2025
2026-02-24T18:18:31.887204831Z 사용 가능 모델: models/deep-research-pro-preview-12-2025
2026-02-24T18:18:31.887208581Z ---------------------------
2026-02-24T18:18:31.887225772Z INFO:     127.0.0.1:51878 - "HEAD / HTTP/1.1" 405 Method Not Allowed
2026-02-24T18:19:35.430397734Z INFO:     Shutting down
2026-02-24T18:19:35.530929603Z INFO:     Waiting for application shutdown.
2026-02-24T18:19:35.531379102Z INFO:     Application shutdown complete.
2026-02-24T18:19:35.531398362Z INFO:     Finished server process [38]
2026-02-24T18:20:05.907051708Z ==> Your service is live 🎉
2026-02-24T18:20:06.50275248Z ==> 
2026-02-24T18:20:06.505322034Z ==> ///////////////////////////////////////////////////////////
2026-02-24T18:20:06.50834188Z ==> 
2026-02-24T18:20:06.511066868Z ==> Available at your primary URL https://persona-ai-sa01.onrender.com
2026-02-24T18:20:06.514043583Z ==> 
2026-02-24T18:20:06.517084668Z ==> ///////////////////////////////////////////////////////////
2026-02-24T18:20:26.894294848Z INFO:     34.82.57.203:0 - "GET / HTTP/1.1" 200 OK
2026-02-24T18:23:14.234720738Z INFO:     121.182.26.226:0 - "GET /check HTTP/1.1" 404 Not Found
2026-02-24T18:23:24.249258459Z INFO:     211.117.24.132:0 - "GET /check HTTP/1.1" 404 Not Found
2026-02-24T18:23:24.7277261Z INFO:     211.117.24.132:0 - "GET /favicon.ico HTTP/1.1" 404 Not Found
2026-02-24T18:23:32.578163941Z INFO:     121.182.26.226:0 - "GET /check HTTP/1.1" 404 Not Found
2026-02-24T18:23:40.841006043Z ==> Detected service running on port 10000
2026-02-24T18:23:42.202136977Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
2026-02-24T18:23:45.002656537Z ==> Deploying...
2026-02-24T18:23:45.274918145Z ==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance
2026-02-24T18:24:11.078337167Z INFO:     121.182.26.226:0 - "GET /check HTTP/1.1" 404 Not Found
2026-02-24T18:24:13.722731344Z ==> Running 'uvicorn app:app --host 0.0.0.0 --port $PORT'
2026-02-24T18:24:20.629623367Z INFO:     121.182.26.226:0 - "GET /check HTTP/1.1" 404 Not Found
2026-02-24T18:24:24.29724686Z INFO:     121.182.26.226:0 - "GET / HTTP/1.1" 200 OK
2026-02-24T18:24:24.493777549Z INFO:     121.182.26.226:0 - "GET /static/script.js HTTP/1.1" 200 OK
2026-02-24T18:24:24.49449774Z INFO:     121.182.26.226:0 - "GET /static/style.css HTTP/1.1" 200 OK
2026-02-24T18:24:26.734380744Z /opt/render/project/src/app.py:7: FutureWarning: 
2026-02-24T18:24:26.734399175Z 
2026-02-24T18:24:26.734404315Z All support for the `google.generativeai` package has ended. It will no longer be receiving 
2026-02-24T18:24:26.734407886Z updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
2026-02-24T18:24:26.734410606Z See README for more details:
2026-02-24T18:24:26.734412536Z 
2026-02-24T18:24:26.734414666Z https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md
2026-02-24T18:24:26.734416606Z 
2026-02-24T18:24:26.734419316Z   import google.generativeai as genai
2026-02-24T18:24:28.132714372Z INFO:     Started server process [57]
2026-02-24T18:24:28.132741524Z INFO:     Waiting for application startup.
2026-02-24T18:24:28.132746864Z INFO:     Application startup complete.
2026-02-24T18:24:28.132981729Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2026-02-24T18:24:29.102826506Z --- 사용 가능한 모델 목록 ---
2026-02-24T18:24:29.102858738Z 사용 가능 모델: models/gemini-2.5-flash
2026-02-24T18:24:29.102864298Z 사용 가능 모델: models/gemini-2.5-pro
2026-02-24T18:24:29.102868719Z 사용 가능 모델: models/gemini-2.0-flash
2026-02-24T18:24:29.102872879Z 사용 가능 모델: models/gemini-2.0-flash-001
2026-02-24T18:24:29.10287791Z 사용 가능 모델: models/gemini-2.0-flash-exp-image-generation
2026-02-24T18:24:29.10288202Z 사용 가능 모델: models/gemini-2.0-flash-lite-001
2026-02-24T18:24:29.10288651Z 사용 가능 모델: models/gemini-2.0-flash-lite
2026-02-24T18:24:29.10289066Z 사용 가능 모델: models/gemini-2.5-flash-preview-tts
2026-02-24T18:24:29.102894951Z 사용 가능 모델: models/gemini-2.5-pro-preview-tts
2026-02-24T18:24:29.102899111Z 사용 가능 모델: models/gemma-3-1b-it
2026-02-24T18:24:29.102903621Z 사용 가능 모델: models/gemma-3-4b-it
2026-02-24T18:24:29.102908381Z 사용 가능 모델: models/gemma-3-12b-it
2026-02-24T18:24:29.102913062Z 사용 가능 모델: models/gemma-3-27b-it
2026-02-24T18:24:29.102917352Z 사용 가능 모델: models/gemma-3n-e4b-it
2026-02-24T18:24:29.102921582Z 사용 가능 모델: models/gemma-3n-e2b-it
2026-02-24T18:24:29.102925942Z 사용 가능 모델: models/gemini-flash-latest
2026-02-24T18:24:29.102930393Z 사용 가능 모델: models/gemini-flash-lite-latest
2026-02-24T18:24:29.102934733Z 사용 가능 모델: models/gemini-pro-latest
2026-02-24T18:24:29.102938833Z 사용 가능 모델: models/gemini-2.5-flash-lite
2026-02-24T18:24:29.102943524Z 사용 가능 모델: models/gemini-2.5-flash-image
2026-02-24T18:24:29.102947804Z 사용 가능 모델: models/gemini-2.5-flash-lite-preview-09-2025
2026-02-24T18:24:29.102952014Z 사용 가능 모델: models/gemini-3-pro-preview
2026-02-24T18:24:29.102956284Z 사용 가능 모델: models/gemini-3-flash-preview
2026-02-24T18:24:29.102960475Z 사용 가능 모델: models/gemini-3.1-pro-preview
2026-02-24T18:24:29.102964605Z 사용 가능 모델: models/gemini-3.1-pro-preview-customtools
2026-02-24T18:24:29.102968825Z 사용 가능 모델: models/gemini-3-pro-image-preview
2026-02-24T18:24:29.102972996Z 사용 가능 모델: models/nano-banana-pro-preview
2026-02-24T18:24:29.102977686Z 사용 가능 모델: models/gemini-robotics-er-1.5-preview
2026-02-24T18:24:29.102981916Z 사용 가능 모델: models/gemini-2.5-computer-use-preview-10-2025
2026-02-24T18:24:29.102986206Z 사용 가능 모델: models/deep-research-pro-preview-12-2025
2026-02-24T18:24:29.102991257Z ---------------------------
2026-02-24T18:24:29.103011278Z INFO:     127.0.0.1:33772 - "HEAD / HTTP/1.1" 405 Method Not Allowed
2026-02-24T18:24:30.357368989Z INFO:     121.182.26.226:0 - "GET /check HTTP/1.1" 404 Not Found
2026-02-24T18:24:37.014571491Z INFO:     121.182.26.226:0 - "GET /check HTTP/1.1" 200 OK
2026-02-24T18:24:37.254922103Z INFO:     121.182.26.226:0 - "GET /favicon.ico HTTP/1.1" 404 Not Found
2026-02-24T18:24:37.447006934Z INFO:     34.82.57.203:0 - "GET / HTTP/1.1" 200 OK
2026-02-24T18:24:37.471881057Z ==> Your service is live 🎉
2026-02-24T18:24:37.711049287Z ==> 
2026-02-24T18:24:37.713805274Z ==> ///////////////////////////////////////////////////////////
2026-02-24T18:24:37.718602685Z ==> 
2026-02-24T18:24:37.721219139Z ==> Available at your primary URL https://persona-ai-sa01.onrender.com
2026-02-24T18:24:37.724064039Z ==> 
2026-02-24T18:24:37.728583813Z ==> ///////////////////////////////////////////////////////////
2026-02-24T18:25:09.087766461Z INFO:     121.182.26.226:0 - "GET / HTTP/1.1" 200 OK
2026-02-24T18:25:14.095170582Z INFO:     121.182.26.226:0 - "GET /check HTTP/1.1" 200 OK
2026-02-24T18:25:35.488320036Z INFO:     Shutting down
2026-02-24T18:25:35.588834775Z INFO:     Waiting for application shutdown.
2026-02-24T18:25:35.588965174Z INFO:     Application shutdown complete.
2026-02-24T18:25:35.589026819Z INFO:     Finished server process [56]
2026-02-24T18:29:04.634979746Z ==> Deploying...
2026-02-24T18:29:04.776532266Z ==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance
2026-02-24T18:29:41.225446218Z ==> Running 'uvicorn app:app --host 0.0.0.0 --port $PORT'
2026-02-24T18:29:53.323053607Z /opt/render/project/src/app.py:7: FutureWarning: 
2026-02-24T18:29:53.323063847Z 
2026-02-24T18:29:53.323066747Z All support for the `google.generativeai` package has ended. It will no longer be receiving 
2026-02-24T18:29:53.323070248Z updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
2026-02-24T18:29:53.323072578Z See README for more details:
2026-02-24T18:29:53.323074208Z 
2026-02-24T18:29:53.323076158Z https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md
2026-02-24T18:29:53.323077718Z 
2026-02-24T18:29:53.323079558Z   import google.generativeai as genai
2026-02-24T18:29:54.916640635Z INFO:     Started server process [56]
2026-02-24T18:29:54.916736171Z INFO:     Waiting for application startup.
2026-02-24T18:29:54.917035319Z INFO:     Application startup complete.
2026-02-24T18:29:54.91737939Z INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
2026-02-24T18:29:55.255376564Z --- 사용 가능한 모델 목록 ---
2026-02-24T18:29:55.255411396Z 사용 가능 모델: models/gemini-2.5-flash
2026-02-24T18:29:55.255415256Z 사용 가능 모델: models/gemini-2.5-pro
2026-02-24T18:29:55.255418186Z 사용 가능 모델: models/gemini-2.0-flash
2026-02-24T18:29:55.255420797Z 사용 가능 모델: models/gemini-2.0-flash-001
2026-02-24T18:29:55.255424917Z 사용 가능 모델: models/gemini-2.0-flash-exp-image-generation
2026-02-24T18:29:55.255427797Z 사용 가능 모델: models/gemini-2.0-flash-lite-001
2026-02-24T18:29:55.255430897Z 사용 가능 모델: models/gemini-2.0-flash-lite
2026-02-24T18:29:55.255433947Z 사용 가능 모델: models/gemini-2.5-flash-preview-tts
2026-02-24T18:29:55.255436578Z 사용 가능 모델: models/gemini-2.5-pro-preview-tts
2026-02-24T18:29:55.255439048Z 사용 가능 모델: models/gemma-3-1b-it
2026-02-24T18:29:55.255441638Z 사용 가능 모델: models/gemma-3-4b-it
2026-02-24T18:29:55.255444608Z 사용 가능 모델: models/gemma-3-12b-it
2026-02-24T18:29:55.255462789Z 사용 가능 모델: models/gemma-3-27b-it
2026-02-24T18:29:55.255469349Z 사용 가능 모델: models/gemma-3n-e4b-it
2026-02-24T18:29:55.25547241Z 사용 가능 모델: models/gemma-3n-e2b-it
2026-02-24T18:29:55.25547489Z 사용 가능 모델: models/gemini-flash-latest
2026-02-24T18:29:55.25547797Z 사용 가능 모델: models/gemini-flash-lite-latest
2026-02-24T18:29:55.255484801Z 사용 가능 모델: models/gemini-pro-latest
2026-02-24T18:29:55.255487781Z 사용 가능 모델: models/gemini-2.5-flash-lite
2026-02-24T18:29:55.255490541Z 사용 가능 모델: models/gemini-2.5-flash-image
2026-02-24T18:29:55.255493301Z 사용 가능 모델: models/gemini-2.5-flash-lite-preview-09-2025
2026-02-24T18:29:55.255496221Z 사용 가능 모델: models/gemini-3-pro-preview
2026-02-24T18:29:55.255499031Z 사용 가능 모델: models/gemini-3-flash-preview
2026-02-24T18:29:55.255501671Z 사용 가능 모델: models/gemini-3.1-pro-preview
2026-02-24T18:29:55.255504562Z 사용 가능 모델: models/gemini-3.1-pro-preview-customtools
2026-02-24T18:29:55.255507232Z 사용 가능 모델: models/gemini-3-pro-image-preview
2026-02-24T18:29:55.255509842Z 사용 가능 모델: models/nano-banana-pro-preview
2026-02-24T18:29:55.255512592Z 사용 가능 모델: models/gemini-robotics-er-1.5-preview
2026-02-24T18:29:55.255515182Z 사용 가능 모델: models/gemini-2.5-computer-use-preview-10-2025
2026-02-24T18:29:55.255517783Z 사용 가능 모델: models/deep-research-pro-preview-12-2025
2026-02-24T18:29:55.255522343Z ---------------------------
2026-02-24T18:29:55.255539834Z INFO:     127.0.0.1:50394 - "HEAD / HTTP/1.1" 405 Method Not Allowed
2026-02-24T18:29:57.552819692Z ==> Your service is live 🎉
2026-02-24T18:29:57.86683737Z ==> 
2026-02-24T18:29:57.872067469Z ==> ///////////////////////////////////////////////////////////
2026-02-24T18:29:57.876791688Z ==> 
2026-02-24T18:29:57.881145499Z ==> Available at your primary URL https://persona-ai-sa01.onrender.com
2026-02-24T18:29:57.888619736Z ==> 
2026-02-24T18:29:57.898100424Z ==> ///////////////////////////////////////////////////////////
2026-02-24T18:29:59.473210614Z INFO:     34.82.41.62:0 - "GET / HTTP/1.1" 200 OK
2026-02-24T18:30:16.055152815Z INFO:     121.182.26.226:0 - "GET / HTTP/1.1" 200 OK
2026-02-24T18:30:16.246736441Z INFO:     121.182.26.226:0 - "GET /static/style.css HTTP/1.1" 200 OK
2026-02-24T18:30:16.538404504Z INFO:     121.182.26.226:0 - "GET /static/script.js HTTP/1.1" 200 OK
2026-02-24T18:30:19.462545822Z Traceback (most recent call last):
2026-02-24T18:30:19.464390325Z   File "/opt/render/project/src/app.py", line 88, in chat
2026-02-24T18:30:19.464401306Z     response = chat_session.send_message(full_prompt)
2026-02-24T18:30:19.464406626Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/generativeai/generative_models.py", line 578, in send_message
2026-02-24T18:30:19.464411286Z     response = self.model.generate_content(
2026-02-24T18:30:19.464416127Z         contents=history,
2026-02-24T18:30:19.464420547Z     ...<5 lines>...
2026-02-24T18:30:19.464424737Z         request_options=request_options,
2026-02-24T18:30:19.464429177Z     )
2026-02-24T18:30:19.464433268Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/generativeai/generative_models.py", line 331, in generate_content
2026-02-24T18:30:19.46446681Z     response = self._client.generate_content(
2026-02-24T18:30:19.46447309Z         request,
2026-02-24T18:30:19.4644771Z         **request_options,
2026-02-24T18:30:19.46448104Z     )
2026-02-24T18:30:19.464485951Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/ai/generativelanguage_v1beta/services/generative_service/client.py", line 835, in generate_content
2026-02-24T18:30:19.464490371Z     response = rpc(
2026-02-24T18:30:19.464494301Z         request,
2026-02-24T18:30:19.464498341Z     ...<2 lines>...
2026-02-24T18:30:19.464502482Z         metadata=metadata,
2026-02-24T18:30:19.464506722Z     )
2026-02-24T18:30:19.464511272Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__
2026-02-24T18:30:19.464515202Z     return wrapped_func(*args, **kwargs)
2026-02-24T18:30:19.464519303Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 294, in retry_wrapped_func
2026-02-24T18:30:19.464523953Z     return retry_target(
2026-02-24T18:30:19.464528013Z         target,
2026-02-24T18:30:19.464532094Z     ...<3 lines>...
2026-02-24T18:30:19.464536434Z         on_error=on_error,
2026-02-24T18:30:19.464540544Z     )
2026-02-24T18:30:19.464544704Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 156, in retry_target
2026-02-24T18:30:19.464548835Z     next_sleep = _retry_error_helper(
2026-02-24T18:30:19.464553095Z         exc,
2026-02-24T18:30:19.464557035Z     ...<6 lines>...
2026-02-24T18:30:19.464560895Z         timeout,
2026-02-24T18:30:19.464565196Z     )
2026-02-24T18:30:19.464569296Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/retry/retry_base.py", line 214, in _retry_error_helper
2026-02-24T18:30:19.464573176Z     raise final_exc from source_exc
2026-02-24T18:30:19.464577596Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/retry/retry_unary.py", line 147, in retry_target
2026-02-24T18:30:19.464581557Z     result = target()
2026-02-24T18:30:19.464585737Z   File "/opt/render/project/src/.venv/lib/python3.14/site-packages/google/api_core/timeout.py", line 130, in func_with_timeout
2026-02-24T18:30:55.230542202Z INFO:     Shutting down
2026-02-24T18:30:55.331022323Z INFO:     Waiting for application shutdown.
2026-02-24T18:30:55.331180533Z INFO:     Application shutdown complete.
2026-02-24T18:30:55.331257508Z INFO:     Finished server process [57]
2026-02-24T18:35:00.379188662Z ==> Detected service running on port 10000
2026-02-24T18:35:00.73021955Z ==> Docs on specifying a port: https://render.com/docs/web-services#port-binding