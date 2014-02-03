from django.contrib.gis.db import models
from picklefield.fields import PickledObjectField

class route(models.Model):
    route_name = models.CharField(max_length=50)
    start_route = models.PointField()
    end_route = models.PointField()
    route_points = PickledObjectField()
    objects = models.GeoManager()

    def __unicode__(self):
        return "%r" % self.route_name

class places(models.Model):
    route = models.ForeignKey(route)
    landmarks = PickledObjectField()
    destination = PickledObjectField()
    objects = models.GeoManager()

    def __unicode__(self):
        return "%r" % self.route.route_name