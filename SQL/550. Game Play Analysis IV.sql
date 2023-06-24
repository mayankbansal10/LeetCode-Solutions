select round((sum(if(datediff(event_date,first_login)=1,1,0))/count(distinct player_id)),2) fraction
from (select *, min(event_date) over(partition by player_id) first_login
      from activity) t