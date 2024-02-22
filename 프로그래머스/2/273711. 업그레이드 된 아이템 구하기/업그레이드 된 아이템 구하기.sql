select i.item_id,item_name,rarity
from item_info as i,(select t.item_id as id
                from item_info,item_tree as t
                where rarity = 'RARE' and item_info.item_id = t.parent_item_id) as o
where i.item_id = id
order by i.item_id desc