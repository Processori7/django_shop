from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery, SearchHeadline

def q_search(query):
    query = query.strip()

    # Поиск по ID, если запрос — короткое число
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    # Если запрос пустой после strip — возвращаем пустой QuerySet
    if not query:
        return Products.objects.none()

    try:
        vector = SearchVector('name', 'description', config='russian')  # Рекомендуется указать язык
        query_obj = SearchQuery(query, config='russian')

        result = (
            Products.objects
            .annotate(rank=SearchRank(vector, query_obj))
            .filter(rank__gt=0)
            .annotate(
                headline=SearchHeadline(
                    'name',
                    query_obj,
                    start_sel='<span style="background-color: yellow;">',
                    stop_sel='</span>',
                )
            )
            .annotate(
                bodyline=SearchHeadline(
                    'description',
                    query_obj,
                    start_sel='<span style="background-color: yellow;">',
                    stop_sel='</span>',
                )
            )
            .order_by('-rank')
        )
        return result 

    except Exception as e:
        return Products.objects.none()  # Возвращаем пустой QuerySet