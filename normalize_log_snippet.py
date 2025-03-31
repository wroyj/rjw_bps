log_path = os.path.join('data', 'logs', 'normalize.log')
with open(log_path, 'a') as log:
    log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Normalized bp_data.csv\n")