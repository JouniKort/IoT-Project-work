using System;
using System.Windows;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Maps.MapControl.WPF;

namespace IOT_Test
{
    class Utils
    {
        private static int LocationIndex = 0;
        public static double TotalDistance = 0;

        public static Location GetLocation(double distance, Location latestLocation,  MapPolyline route)
        {
            double dRoute = CalculateDistance(
                latestLocation.Latitude, latestLocation.Longitude,
                route.Locations[LocationIndex + 1].Latitude, route.Locations[LocationIndex + 1].Longitude);
            if (dRoute < distance)
            {
                LocationIndex++;
                TotalDistance += dRoute;
                return GetLocation(distance - dRoute, route.Locations[LocationIndex], route);
            }
            else
            {
                Location loc = DistanceToLocation(
                    distance,
                    latestLocation.Latitude, latestLocation.Longitude,
                    route.Locations[LocationIndex + 1].Latitude, route.Locations[LocationIndex + 1].Longitude);
                dRoute = CalculateDistance(
                latestLocation.Latitude, latestLocation.Longitude,
                loc.Latitude, loc.Longitude);
                TotalDistance += dRoute;
                return loc;
            }
        }

        private static Location DistanceToLocation(double d, double lat1, double lon1, double lat2, double lon2)
        {
            var R = 6371; // Radius of the earth in km
            var dLat = lat2 - lat1;
            var dLon = lon2 - lon1;

            Vector u = new Vector(dLon, dLat);
            u.Normalize();

            d = 180 * d / (Math.PI * R) * 2;

            return new Location(lat1 + u.Y * d, lon1 + u.X * d);
        }

        private static double CalculateDistance(double lat1, double lon1, double lat2, double lon2)
        {
            var R = 6371; // Radius of the earth in km
            var dLat = deg2rad(lat2 - lat1);
            var dLon = deg2rad(lon2 - lon1);
            var a =
              Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
              Math.Cos(deg2rad(lat1)) * Math.Cos(deg2rad(lat2)) *
              Math.Sin(dLon / 2) * Math.Sin(dLon / 2)
              ;
            var c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
            var d = R * c; // Distance in km
            return d;
        }

        private static double deg2rad(double deg)
        {
            return deg * (Math.PI / 180);
        }

        private static double rad2deg(double rad)
        {
            return rad * 180 / Math.PI;
        }
    }
}
