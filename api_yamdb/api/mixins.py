from rest_framework import mixins, viewsets


class CustomViewSetMixins(mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass
