                   List of relations
 Schema |            Name            | Type  |  Owner
--------+----------------------------+-------+----------
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | cce_tb                     | table | postgres
 public | complaint_tb               | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
 public | location_tb                | table | postgres
 public | manager_tb                 | table | postgres
 public | productcategory_tb         | table | postgres
 public | productmodels_tb           | table | postgres
 public | technician_tb              | table | postgres
 public | workreport_tb              | table | postgres
(18 rows)

smt=# select * from technician_tb;
 id | tec_name | tec_phone |   tec_email    | tec_age | tec_gender | tec_Address  | tec_location |          tec_photo          | tec_jdate  | tec_password
----+----------+-----------+----------------+---------+------------+--------------+--------------+-----------------------------+------------+--------------
 13 | tec1     | 56465     | 7868           |      23 | Male       | fdhgfhfghgfj | Alappuzha    | technician/user_189XZEW.png | 2023-03-27 | pwd
 14 | tec2     | 87484     | tec2@gmail.com |      24 | Male       | fgjfjhgg     | Eranakulam   | technician/user_f8PFppQ.png | 2023-03-22 | pwd
 15 | tec7     | 7777777   | tec7@gmail.com |      27 | Male       | assfghg      | Malappuram   | technician/user_bR2CK9p.png | 2023-03-27 | pwd


 smt=# select * from cce_tb;
 id | cce_name | cce_phone |   cce_email    | cce_age | cce_gender | cce_Address |      cce_photo       | cce_jdate  | cce_password
----+----------+-----------+----------------+---------+------------+-------------+----------------------+------------+--------------
  1 | jgj      | 75765     | fgdg@gmail     |      23 | Female     | hmkjhkj\r  +| cce/user.png         | 2023-03-25 | as
    |          |           |                |         |            | ghjkhjkjh\r+|                      |            |
    |          |           |                |         |            |             |                      |            |
  2 | cce2     | 66557     | cce2@gmail.com |      22 | Female     | ehtyjgjdg\r+| cce/user_ByC67O3.png | 2023-03-25 | pwd
    |          |           |                |         |            | dhhfh\r    +|                      |            |
    |          |           |                |         |            | fdhfhfh\r  +|                      |            |
    |          |           |                |         |            |             |                      |            |
  3 | cce3     | 9866      | cce3@gmail.com |      25 | Female     | jkhjkh\r   +| cce/user_eb31jJx.png | 2023-03-25 | cce3p



smt=# select * from complaint_tb;
 id | customer_name | customer_phone1 | customer_phone2 |  customer_email  | customer_address | customer_location | category_name | model_name | complaint_des | purchase_date |          complaint_date          | warrenty | physical_damage | technician_name | work_status | complaint_name | category_id | cce_id | location_id | model_id | technician_id | remark

----+---------------+-----------------+-----------------+------------------+------------------+-------------------+---------------+------------+---------------+---------------+----------------------------------+----------+-----------------+-----------------+-------------+----------------+-------------+--------+-------------+----------+---------------+--------
 11 | cu1           | 3344            | 3344            | cu1@gmail.com    | ghghfhf          | Alappuzha         | LED TV        | LED32      | cc            | 2023-03-20    | 2023-03-27 18:26:10.651627+05:30 | true     | false           | tec1            | new         | 9465           |           1 |      2 |           1 |        1 |            13 |
 12 | cu2           | 9999999         | 9999999         | cu2@gmail.com    | gghfghh          | Eranakulam        | LED TV        | LED32      | fgdfg         | 2023-03-03    | 2023-03-27 18:28:01.695932+05:30 | true     | false           | tec2            | new         | 1691           |           1 |      2 |           2 |        1 |            14 |
 13 | cu4           | 4444            | 4444            | cu4@gmail.com    | ghhj             | Eranakulam        | LED TV        | LED32      | cx            | 2023-03-08    | 2023-03-27 18:30:18.612726+05:30 | true     | false           | tec2            | new         | 1962           |           1 |      2 |           2 |        1 |            14 |
 14 | cu3           | 66666           | 66666           | cu3@gmail.com    | hjkk             | Alappuzha         | LED TV        | LED32      | jl            | 2023-03-15    | 2023-03-27 18:32:29.813584+05:30 | true     | false           | tec1            | new         | 6525           |           1 |      2 |           1 |        1 |            13 |
 15 | cu3333        | 6565568         | 6565568         | cu3333@gmail.com | hghj             | Malappuram        | LED TV        | WSM75      | gfvjh         | 2023-03-07    | 2023-03-28 06:58:17.066505+05:30 | true     | false           | tec7            | new         | 9016           |           1 |      2 |           8 |        4 |            15 |
(5 rows)


smt=# select * from workreport_tb;
 id | complaint_name | description | work_date | work_time | serial_number | warrenty | work_status | serviece_charge | travel_distance | complaint_id | technician_id
----+----------------+-------------+-----------+-----------+---------------+----------+-------------+-----------------+-----------------+--------------+---------------
(0 rows)




smt=# select * from technician_tb;
 id | tec_name | tec_phone |   tec_email    | tec_age | tec_gender | tec_Address  | tec_location |          tec_photo          | tec_jdate  | tec_password
----+----------+-----------+----------------+---------+------------+--------------+--------------+-----------------------------+------------+--------------
 13 | tec1     | 56465     | 7868           |      23 | Male       | fdhgfhfghgfj | Alappuzha    | technician/user_189XZEW.png | 2023-03-27 | pwd
 14 | tec2     | 87484     | tec2@gmail.com |      24 | Male       | fgjfjhgg     | Eranakulam   | technician/user_f8PFppQ.png | 2023-03-22 | pwd
 15 | tec7     | 7777777   | tec7@gmail.com |      27 | Male       | assfghg      | Malappuram   | technician/user_bR2CK9p.png | 2023-03-27 | pwd
 16 | Arun     | 34456477  | arun@gmail.com |      25 | Mal        | xfg house\r +| Kozhikode    | technician/user_JpC3JV1.png | 2023-03-27 | arunp



                   List of relations
 Schema |            Name            | Type  |  Owner
--------+----------------------------+-------+----------
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | cce_tb                     | table | postgres
 public | complaint_tb               | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
 public | location_tb                | table | postgres
 public | manager_tb                 | table | postgres
 public | productcategory_tb         | table | postgres
 public | productmodels_tb           | table | postgres
 public | technician_tb              | table | postgres
 public | workreport_tb              | table | postgres
(18 rows)




select * from location_tb;
 id |  location
----+------------
  1 | Alappuzha
  3 | Idukki
  4 | Kasaragod
  5 | Kollam
  6 | Kottayam
  7 | Kozhikode
  8 | Malappuram
  2 | Eranakulam



  insert into location_tb (location) values ('Kannur'),('Palakkad'),('Pathanamthitta'),('Thiruvananthapuram'),('Thrissur'),('Wayanad')




smt=# select * from technician_tb;
 id | tec_name | tec_phone |   tec_email    | tec_age | tec_gender | tec_Address  | tec_location |          tec_photo          | tec_jdate  | tec_password
----+----------+-----------+----------------+---------+------------+--------------+--------------+-----------------------------+------------+--------------
 13 | tec1     | 56465     | 7868           |      23 | Male       | fdhgfhfghgfj | Alappuzha    | technician/user_189XZEW.png | 2023-03-27 | pwd
 14 | tec2     | 87484     | tec2@gmail.com |      24 | Male       | fgjfjhgg     | Eranakulam   | technician/user_f8PFppQ.png | 2023-03-22 | pwd
 15 | tec7     | 7777777   | tec7@gmail.com |      27 | Male       | assfghg      | Malappuram   | technician/user_bR2CK9p.png | 2023-03-27 | pwd
 16 | Arun     | 34456477  | arun@gmail.com |      25 | Mal        | xfg house\r +| Kozhikode    | technician/user_JpC3JV1.png | 2023-03-27 | arunp
    |          |           |                |         |            | kozhikode    |              |                             |            |
(4 rows)



insert into productcategory_tb  (category) values ('Induction Cooker'),('Home theatre'),('Microwave Oven');