from django.db import models


class ManagerMain(models.Manager):
    def get_queryset(self, **kwargs):
        return super(ManagerMain, self).get_queryset() \
            .filter(deleted_at__isnull=True, **kwargs)


class ManagerAllMain(models.Manager):
    def get_queryset(self):
        return super(ManagerAllMain, self).get_queryset()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = ManagerMain()
    objects_all = ManagerAllMain()

    class Meta:
        abstract = True


class ContextDataMixin(object):
    context_object_name = None

    def get_queryset(self):
        return self.model.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        kwargs.update({self.context_object_name: self.get_queryset()})
        return super(ContextDataMixin, self).get_context_data(**kwargs)
