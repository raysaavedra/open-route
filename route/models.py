from django.contrib.gis.db import models

class route(models.Model):
    route_name = models.CharField(max_length=50)
    start_point = models.PointField()
    end_point = models.PointField()
    route_points = models.GeometryField()
    destination = models.TextField()
    objects = models.GeoManager()

    def __unicode__(self):
        return "%r" % self.route_name