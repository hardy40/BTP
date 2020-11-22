def implicit():
    from google.cloud import storage

    sc = storage.Client()

    buckets = list(sc.list_buckets())
    print (buckets)

implicit()