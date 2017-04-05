<?php $ctx = json_decode(file_get_contents('php://input')); ?>
<head>
    <title>Comments</title>
</head>
<body>
    <?php foreach($ctx->comments as $comment): ?>
        <pre><?php echo $comment->comment ?></pre>
        - <?php echo $comment->name ?><br />
        <br />
    <?php endforeach; ?>
    <?php if(!sizeof($ctx->comments)): ?>
        <div>no comments</div>
    <?php endif; ?>
    <br />
    <br />
    <form method="POST" />
    <?php echo $ctx->csrf_token ?>
    <?php echo $ctx->form ?>
    <input type="submit" value="Submit" />
    </form>
</body>

