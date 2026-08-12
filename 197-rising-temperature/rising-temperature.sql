-- Write your PostgreSQL query statement below
SELECT today.id FROM Weather as today
WHERE EXISTS
    (SELECT 1 FROM Weather as yesterday
        WHERE 
            today.temperature > yesterday.temperature
            AND
            today.recordDate - yesterday.recordDate = 1);