import pytest
import os
import tempfile
import yaml
from unittest.mock import patch
from src.utils import load_config, delete_directory, clear_directory


class TestLoadConfig:
    """测试 load_config 函数"""

    def test_load_config_success(self):
        """测试成功加载配置文件"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            test_config = {
                'api': {
                    'base_url': 'http://test.com',
                    'api_key': 'test_key'
                },
                'database': {
                    'host': 'localhost',
                    'port': 5432
                }
            }
            yaml.dump(test_config, f)
            config_file = f.name

        try:
            config = load_config(config_file)
            assert config is not None
            assert config['api']['base_url'] == 'http://test.com'
            assert config['api']['api_key'] == 'test_key'
            assert config['database']['host'] == 'localhost'
            assert config['database']['port'] == 5432
        finally:
            os.unlink(config_file)

    def test_load_config_file_not_found(self):
        """测试配置文件不存在的情况"""
        config = load_config('nonexistent_config.yaml')
        assert config == {}

    def test_load_config_invalid_yaml(self):
        """测试无效的 YAML 文件"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write('invalid: yaml: content:')
            config_file = f.name

        try:
            config = load_config(config_file)
            assert config == {}
        finally:
            os.unlink(config_file)

    def test_load_config_empty_file(self):
        """测试空配置文件"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            config_file = f.name

        try:
            config = load_config(config_file)
            assert config is None
        finally:
            os.unlink(config_file)


class TestDeleteDirectory:
    """测试 delete_directory 函数"""

    def test_delete_directory_success(self):
        """测试删除目录 - 成功"""
        with tempfile.TemporaryDirectory() as parent_dir:
            test_dir = os.path.join(parent_dir, 'test_delete_dir')
            os.makedirs(test_dir)
            
            with open(os.path.join(test_dir, 'file1.txt'), 'w') as f:
                f.write('content1')
            os.makedirs(os.path.join(test_dir, 'subdir'))
            with open(os.path.join(test_dir, 'subdir', 'file2.txt'), 'w') as f:
                f.write('content2')
            
            delete_directory(test_dir)
            
            assert not os.path.exists(test_dir)

    def test_delete_directory_nonexistent(self):
        """测试删除目录 - 目录不存在"""
        nonexistent_dir = '/tmp/nonexistent_directory_12345'
        
        if os.path.exists(nonexistent_dir):
            os.rmdir(nonexistent_dir)
        
        delete_directory(nonexistent_dir)
        
        assert not os.path.exists(nonexistent_dir)

    def test_delete_directory_with_nested_structure(self):
        """测试删除目录 - 嵌套结构"""
        with tempfile.TemporaryDirectory() as parent_dir:
            test_dir = os.path.join(parent_dir, 'nested_dir')
            os.makedirs(os.path.join(test_dir, 'level1', 'level2', 'level3'))
            
            delete_directory(test_dir)
            
            assert not os.path.exists(test_dir)

    @patch('src.utils.shutil.rmtree')
    def test_delete_directory_error(self, mock_rmtree):
        """测试删除目录 - 删除失败"""
        mock_rmtree.side_effect = PermissionError('Permission denied')
        test_dir = '/tmp/delete_directory_error'

        with patch('src.utils.os.path.exists', return_value=True):
            delete_directory(test_dir)

        mock_rmtree.assert_called_once_with(test_dir)


class TestClearDirectory:
    """测试 clear_directory 函数"""

    def test_clear_directory_success(self):
        """测试清空目录 - 成功"""
        with tempfile.TemporaryDirectory() as test_dir:
            with open(os.path.join(test_dir, 'file1.txt'), 'w') as f:
                f.write('content1')
            with open(os.path.join(test_dir, 'file2.txt'), 'w') as f:
                f.write('content2')
            
            clear_directory(test_dir, '')
            
            assert os.path.exists(test_dir)
            assert len(os.listdir(test_dir)) == 0

    def test_clear_directory_with_ignore_file(self):
        """测试清空目录 - 忽略文件"""
        with tempfile.TemporaryDirectory() as test_dir:
            with open(os.path.join(test_dir, 'ignore.txt'), 'w') as f:
                f.write('keep this')
            with open(os.path.join(test_dir, 'delete.txt'), 'w') as f:
                f.write('delete this')
            
            clear_directory(test_dir, 'ignore.txt')
            
            assert os.path.exists(test_dir)
            assert 'ignore.txt' in os.listdir(test_dir)
            assert 'delete.txt' not in os.listdir(test_dir)

    def test_clear_directory_nonexistent(self):
        """测试清空目录 - 目录不存在"""
        nonexistent_dir = '/tmp/nonexistent_clear_dir_12345'
        
        if os.path.exists(nonexistent_dir):
            import shutil
            shutil.rmtree(nonexistent_dir)
        
        clear_directory(nonexistent_dir, None)
        
        assert not os.path.exists(nonexistent_dir)

    def test_clear_directory_with_subdirectories(self):
        """测试清空目录 - 包含子目录"""
        with tempfile.TemporaryDirectory() as test_dir:
            subdir = os.path.join(test_dir, 'subdir')
            os.makedirs(subdir)
            with open(os.path.join(subdir, 'file.txt'), 'w') as f:
                f.write('content')
            
            clear_directory(test_dir, '')
            
            assert os.path.exists(test_dir)
            assert os.path.exists(subdir)
            assert len(os.listdir(subdir)) == 0
