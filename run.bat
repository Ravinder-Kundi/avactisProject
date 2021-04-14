python -m pytest -s -v -m "sanity" --alluredir="C:\Users\rubyk\PycharmProjects\avactis automation\Reports\allure_report" testCases/



rem pytest -s -v -m "sanity"  --html=Reports/report.html testCases/

rem pytest -s -v -m "regression"  --html=Reports/report.html testCases/


rem pytest -s -v -m "sanity"or "regression"  --html=Reports/report.html testCases/

rem pytest -s -v -m "regression" and "sanity" --html=Reports/report.html testCases/
