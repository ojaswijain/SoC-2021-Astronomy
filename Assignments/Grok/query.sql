select s.radius, count(Planet.koi_name)
from Star as s
Join planet using (kepler_id)
where s.radius>=1
group by s.kepler_id
having count(Planet.koi_name)>1
order by s.radius desc
