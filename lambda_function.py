import boto3
import datetime

def lambda_handler(event, context):
    # Создайте клиент для AWS Cost Explorer
    ce = boto3.client('ce')

    # Получите текущую дату
    end_date = datetime.datetime.utcnow()
    start_date = end_date.replace(day=1)

    # Форматирование временного периода в нужный формат
    formatted_start_date = start_date.strftime('%Y-%m-%d')
    formatted_end_date = end_date.strftime('%Y-%m-%d')

    # Запрос на получение расходов за текущий месяц
    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': formatted_start_date,
            'End': formatted_end_date
        },
        Granularity='MONTHLY',
        Metrics=['BlendedCost']
    )

    # Вывод информации о расходах
    return response