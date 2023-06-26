SELECT IF(MOD(id,2)=0,id-1,IF(id<(SELECT MAX(ID) FROM Seat),id+1,id)) as id, student 
from Seat ORDER BY id;