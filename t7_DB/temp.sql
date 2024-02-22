update products set prod_name = 'ноутбук ibm'
where prod_name = 'ноутбук imb';


update orders o set reg_date = '2023-01-01'
where ord_id = 1; 

update orders o set reg_date = '2023-02-01'
where ord_id = 2; 
update orders o set reg_date = '2023-03-01'
where ord_id = 3; 
update orders o set reg_date = '2023-04-01'
where ord_id = 4; 
update orders o set reg_date = '2023-05-01'
where ord_id = 5; 
update orders o set reg_date = '2023-06-01'
where ord_id = 6; 
update orders o set reg_date = '2023-07-01'
where ord_id = 7; 
update orders o set reg_date = '2023-08-01'
where ord_id = 8; 
update orders o set reg_date = '2023-09-01'
where ord_id = 9; 
update orders o set date_of_completion = '2023-01-03'
where ord_id = 1; 


select distinct c.fio from clients c 
join orders o on o.cl_id = c.cl_id;

select distinct e.job_title from employees e 
where e.job_title like 'менеджер%';

select distinct pr.pa_name, count(d.pr_id) as del_count from delivery d 
join provider pr on d.pr_id = pr.pr_id
group by pr.pa_name 
order by del_count desc;

-- запрос возвращает самого ценного покупателя 
select c.fio, sum(p.selling_price - p.purchase_price) as margin from orders o
join clients c on o.cl_id = c.cl_id
join products p on o.prod_id = p.prod_id
group by c.fio 
order by margin desc;


SELECT *
FROM   pg_indexes
WHERE  schemaname = 'public' -- замените на имя вашей схемы, если необходимо
AND    tablename = 'orders' -- замените на имя нужной таблицы
ORDER  BY indexname;


alter table products add total_cost decimal(10, 2); 

CREATE OR REPLACE FUNCTION update_total_cost()
  RETURNS TRIGGER AS $$
BEGIN
  UPDATE products SET total_cost = selling_price * amount
  WHERE prod_id = NEW.prod_id;
  RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

CREATE TRIGGER trigger_update_total_cost
  AFTER UPDATE ON products
  FOR EACH ROW WHEN (NEW.amount <> OLD.amount)
  EXECUTE PROCEDURE update_total_cost();

update products set amount= amount-1
 where prod_id = 1;

DELETE FROM pg_trigger
WHERE tgname = 'trigger_update_total_cost'
AND tgrelid = 'products'::regclass;