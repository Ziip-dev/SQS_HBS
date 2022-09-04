-- @block Bookmarked query
-- @group SQS_HBS
-- @name test update continu

SELECT fitapp_timeseriesdata.date,
       auth_user.username,
       fitapp_timeseriesdatatype.resource,
       fitapp_timeseriesdata.value

FROM fitapp_timeseriesdata
JOIN auth_user ON fitapp_timeseriesdata.user_id=auth_user.id
JOIN fitapp_timeseriesdatatype ON fitapp_timeseriesdata.resource_type_id=fitapp_timeseriesdatatype.id

WHERE fitapp_timeseriesdata.date >= '2022-08-20'
AND (fitapp_timeseriesdatatype.resource = 'minutesFairlyActive'
  OR fitapp_timeseriesdatatype.resource = 'minutesVeryActive')

ORDER BY fitapp_timeseriesdata.date ASC
