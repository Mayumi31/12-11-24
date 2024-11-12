# Selection Sort: Sort by Salary
def selection_sort(applications, key, reverse=False):
    n = len(applications)
    for i in range(n):
        selected = i
        for j in range(i + 1, n):
            try:
                # Compare values with `get` to handle missing keys
                if (applications[j].get(key, float('inf')) < applications[selected].get(key, float('inf'))) != reverse:
                    selected = j
            except KeyError:
                continue  # Skip if key is missing
        # Swap if a new selected index was found
        applications[i], applications[selected] = applications[selected], applications[i]
    return applications

def shell_sort(applications, key, reverse=False):
    n = len(applications)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = applications[i]
            j = i
            # Compare using the provided key
            while j >= gap and (applications[j - gap][key] > temp[key]) != reverse:
                applications[j] = applications[j - gap]
                j -= gap
            applications[j] = temp
        gap //= 2
    
    return applications

def bucket_sort_with_selection(applications, key, reverse=False):
    # Creating buckets for the provided key
    buckets = {}
    for app in applications:
        bucket_key = app[key]
        if bucket_key not in buckets:
            buckets[bucket_key] = []
        buckets[bucket_key].append(app)
    
    # Sort each bucket using selection sort
    sorted_apps = []
    for bucket_key in sorted(buckets, reverse=reverse):
        sorted_bucket = selection_sort(buckets[bucket_key], key, reverse)
        sorted_apps.extend(sorted_bucket)
    
    return sorted_apps

def bucket_sort_with_shell(applications, key, reverse=False):
    # Creating buckets for the provided key
    buckets = {}
    for app in applications:
        bucket_key = app[key]
        if bucket_key not in buckets:
            buckets[bucket_key] = []
        buckets[bucket_key].append(app)
    
    # Sort each bucket using shell sort
    sorted_apps = []
    for bucket_key in sorted(buckets, reverse=reverse):
        sorted_bucket = shell_sort(buckets[bucket_key], key, reverse)
        sorted_apps.extend(sorted_bucket)
    
    return sorted_apps
