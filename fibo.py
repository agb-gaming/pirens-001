def lambda_handler(event, context):
    
    n = event.get('n', 10)  

    fib_series = []
    a, b = 0, 1

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
      
    return {
        'statusCode': 200,
        'body': {
            'FibonacciSeries': fib_series
        }
    }
