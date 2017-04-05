TEST<br />
<?php $data = json_decode(file_get_contents('php://input')); ?>
<?php foreach ($data->items as $item): ?>
    <?php echo $item ?><br />
<?php endforeach; ?>
