from versions.default import *

class Forge(Server):
    """Forge (1.17) needs to be run with:\n\t `java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.17.1-37.0.34/win_args.txt`"""

    def __init__(version_number:str) -> str:

        """Forge (1.17) needs to be run with:\n\t `java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.17.1-37.0.34/win_args.txt`"""
        

        versions = {

            '1.10':'https://www.mediafire.com/file/6snfadeewc793lw/1.10.zip/file',

            '1.11':'https://www.mediafire.com/file/xvvb9in54d796gn/1.11.zip/file',

            '1.12':'https://www.mediafire.com/file/pe37eb5n4057wpi/1.12.zip/file',

            '1.13':'https://www.mediafire.com/file/u8amzgd1g2alymb/1.13.zip/file',

            '1.14':'https://www.mediafire.com/file/tc83e2fiz2tn18p/1.14.zip/file',

            '1.5':'https://www.mediafire.com/file/7sjhh2a38sysrka/1.5.zip/file',

            '1.6':'https://www.mediafire.com/file/7jicblntdjovg5l/1.6.zip/file',

            '1.8':'https://www.mediafire.com/file/6dz2e7f8b6k8jac/1.8.9.zip/file',

            '1.9':'https://www.mediafire.com/file/v05hi3sd3fsdee9/1.9.4.zip/file',

            '1.15':'https://www.mediafire.com/file/mp0zl0eho6zqrrl/1.15.zip/file',

            '1.16':'https://www.mediafire.com/file/cjt28k8t7z0g5so/1.16.zip/file',

            '1.17':'https://www.mediafire.com/file/i3b3bm4rb8ubrvv/1.17.zip/file'
        }

        version = versions.keys()
        if version_number in version:
            download_url = versions[version_number]
            return download_url
        else:
            print()
            print(f'The version "{version_number}" is not found!')
            print()
            return "about:blank"